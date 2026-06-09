FROM grafana/alloy:v1.3.1

RUN addgroup --system alloy && \
    adduser --system --ingroup alloy alloy

USER alloy


COPY config.alloy /etc/alloy/config.alloy
CMD ["run", "/etc/alloy/config.alloy"]