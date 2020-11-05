%global packname  IFAA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Analysis for Absolute Abundance in Microbiome

License:          GNU General Public License version 2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.3.0
BuildRequires:    R-parallel >= 3.3.0
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-Matrix >= 1.2.14
BuildRequires:    R-CRAN-picasso >= 1.2.0
BuildRequires:    R-CRAN-future >= 1.12.0
BuildRequires:    R-CRAN-HDCI >= 1.0.2
BuildRequires:    R-CRAN-doParallel >= 1.0.11
BuildRequires:    R-CRAN-mathjaxr >= 1.0.1
BuildRequires:    R-CRAN-expm >= 0.999.3
BuildRequires:    R-CRAN-rlecuyer >= 0.3.3
Requires:         R-methods >= 3.3.0
Requires:         R-parallel >= 3.3.0
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-Matrix >= 1.2.14
Requires:         R-CRAN-picasso >= 1.2.0
Requires:         R-CRAN-future >= 1.12.0
Requires:         R-CRAN-HDCI >= 1.0.2
Requires:         R-CRAN-doParallel >= 1.0.11
Requires:         R-CRAN-mathjaxr >= 1.0.1
Requires:         R-CRAN-expm >= 0.999.3
Requires:         R-CRAN-rlecuyer >= 0.3.3

%description
A novel approach to make inference on the association of covariates with
the absolute abundance (AA) of 'microbiome' in an ecosystem. It can be
also directly applied to relative abundance (RA) data to make inference on
AA because the ratio of two RA is equal ratio of their AA. This algorithm
can estimate and test the associations of interest while adjusting for
potential 'confounders'. The estimates of this method have easy
interpretation like a typical regression analysis. High-dimensional
covariates are handled with regularization and it is implemented by
parallel computing. This algorithm finds optimal reference 'taxa/OTU
(Operational Taxonomic Unit)/ASV (Amplicon Sequence Bariant)' and uses
permutation to control FDR (False Discovery Rate) as described in Zhigang
Li, et al. (2020) <arXiv:1909.10101v3>, Zhigang Li, et al. (2018)
<doi:10.1007/s12561-018-9219-2>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
