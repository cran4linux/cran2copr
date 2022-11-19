%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EGRNi
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Ensemble Gene Regulatory Network Inference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fdrtool 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-stats 
Requires:         R-CRAN-fdrtool 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-readr 
Requires:         R-stats 

%description
Gene regulatory network constructed using combined score obtained from
individual network inference method. The combined score measures the
significance of edges in the ensemble network. Fisher's weighted method
has been implemented to combine the outcomes of different methods based on
the probability values. The combined score follows chi-square distribution
with 2n degrees of freedom. <doi:10.22271/09746315.2020.v16.i3.1358>.

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
