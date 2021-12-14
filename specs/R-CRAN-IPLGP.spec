%global __brp_check_rpaths %{nil}
%global packname  IPLGP
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Identification of Parental Lines via Genomic Prediction

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sommer 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sommer 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Combining genomic prediction with Monte Carlo simulation, three different
strategies are implemented to select parental lines for multiple traits in
plant breeding. The selection strategies include (i) GEBV-O considers only
genomic estimated breeding values (GEBVs) of the candidate individuals;
(ii) GD-O considers only genomic diversity (GD) of the candidate
individuals; and (iii) GEBV-GD considers both GEBV and GD. The above
method can be seen in Chung PY, Liao CT (2020)
<doi:10.1371/journal.pone.0243159>. Multi-trait genomic best linear
unbiased prediction (MT-GBLUP) model is used to simultaneously estimate
GEBVs of the target traits, and then a selection index is adopted to
evaluate the composite performance of an individual.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
