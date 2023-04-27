ARG VERSION=rawhide
FROM registry.fedoraproject.org/fedora:$VERSION AS r-fedora

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
    && dnf -y clean all \
    && echo "options(repos='https://cloud.r-project.org')" > \
        /usr/lib64/R/etc/Rprofile.site

# install littler scripts
RUN dnf -y install R-CRAN-{littler,remotes} \
    && dnf -y clean all \
    && ln -s /usr/local/lib/R/library /usr/local/lib/R/site-library \
    && ln -s /usr/local/lib/R/library/littler/examples/install.r \
        /usr/local/bin/install.r \
    && ln -s /usr/local/lib/R/library/littler/examples/install2.r \
        /usr/local/bin/install2.r \
    && ln -s /usr/local/lib/R/library/littler/examples/installGithub.r \
        /usr/local/bin/installGithub.r \
    && ln -s /usr/local/lib/R/library/littler/examples/testInstalled.r \
        /usr/local/bin/testInstalled.r

FROM r-fedora AS r-copr

# enable manager
RUN mv /usr/lib64/R/etc/Rprofile.site /usr/lib64/R/etc/Rprofile.site.bkp \
    && dnf -y install R-CoprManager \
    && dnf -y clean all \
    && mv /usr/lib64/R/etc/Rprofile.site.bkp /usr/lib64/R/etc/Rprofile.site.d/00-repos.site
