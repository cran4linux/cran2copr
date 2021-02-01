FROM fedora:33

LABEL org.label-schema.license="GPL-2.0" \
      org.label-schema.vcs-url="https://github.com/Enchufa2/cran2copr" \
      maintainer="Iñaki Ucar <iucar@fedoraproject.org>"

RUN sed -ie '/nodocs/d' /etc/dnf/dnf.conf
RUN echo "install_weak_deps=False" >> /etc/dnf/dnf.conf \
    && dnf install -y R-devel sudo

RUN dnf install -y 'dnf-command(copr)' \
    && dnf copr enable iucar/cran -y \
    && dnf install -y R-CoprManager \
    && echo "options(bspm.sudo=TRUE)" > \
        /usr/lib64/R/etc/Rprofile.site.d/50-CoprManager-sudo.site

RUN useradd -m docker \
    && echo "docker ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/docker-user \
    && chmod 0440 /etc/sudoers.d/docker-user \
    && mkdir -p /usr/local/lib/R/library \
    && chown 1000:1000 /usr/local/lib/R/library

RUN dnf install -y R-littler-examples \
    && ln -s /usr/lib64/R/library/littler/examples/install.r \
        /usr/local/bin/install.r \
    && install.r remotes

CMD ["bash"]
