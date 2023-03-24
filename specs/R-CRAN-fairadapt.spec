%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fairadapt
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Fair Data Adaptation with Quantile Preservation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ranger >= 0.13.1
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-qrnn 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ranger >= 0.13.1
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-qrnn 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-scales 

%description
An implementation of the fair data adaptation with quantile preservation
described in Plecko & Meinshausen (2019) <arXiv:1911.06685>. The
adaptation procedure uses the specified causal graph to pre-process the
given training and testing data in such a way to remove the bias caused by
the protected attribute. The procedure uses tree ensembles for quantile
regression.

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
