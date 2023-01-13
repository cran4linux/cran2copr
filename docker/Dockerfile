ARG VERSION=rawhide
FROM registry.fedoraproject.org/fedora:$VERSION

LABEL org.opencontainers.image.licenses="GPL-2.0" \
      org.opencontainers.image.source="https://github.com/Enchufa2/cran2copr" \
      org.opencontainers.image.authors="Iñaki Ucar <iucar@fedoraproject.org>"

# install R
RUN echo "install_weak_deps=False" >> /etc/dnf/dnf.conf \
    && dnf -y install R-core-devel \
    && dnf -y clean all

# enable copr
RUN dnf -y install 'dnf-command(copr)' \
    && dnf -y copr enable iucar/cran \
    && sed -ie '/nodocs/d' /etc/dnf/dnf.conf \
    && dnf -y install R-CoprManager \
    && dnf -y clean all \
    && echo "options(repos='https://cloud.r-project.org')" > \
        /usr/lib64/R/etc/Rprofile.site.d/00-repos.site

# install littler scripts
RUN dnf -y install R-littler-examples R-remotes \
    && dnf -y clean all \
    && ln -s /usr/lib64/R/library/littler/examples/install.r \
        /usr/local/bin/install.r \
    && ln -s /usr/lib64/R/library/littler/examples/install2.r \
        /usr/local/bin/install2.r \
    && ln -s /usr/lib64/R/library/littler/examples/installGithub.r \
        /usr/local/bin/installGithub.r \
    && ln -s /usr/lib64/R/library/littler/examples/testInstalled.r \
        /usr/local/bin/testInstalled.r

CMD ["bash"]
