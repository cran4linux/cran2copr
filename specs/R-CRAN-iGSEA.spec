%global __brp_check_rpaths %{nil}
%global packname  iGSEA
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Integrative Gene Set Enrichment Analysis Approaches

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
To integrate multiple GSEA studies, we propose a hybrid strategy,
iGSEA-AT, for choosing random effects (RE) versus fixed effect (FE)
models, with an attempt to achieve the potential maximum statistical
efficiency as well as stability in performance in various practical
situations. In addition to iGSEA-AT, this package also provides options to
perform integrative GSEA with testing based on a FE model (iGSEA-FE) and
testing based on a RE model (iGSEA-RE). The approaches account for
different set sizes when testing a database of gene sets. The function is
easy to use, and the three approaches can be applied to both binary and
continuous phenotypes.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
