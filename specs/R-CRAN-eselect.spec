%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eselect
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Clinical Trial Designs with Endpoint Selection and Sample Size Reassessment

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-CompAREdesign 
Requires:         R-stats 
Requires:         R-CRAN-CompAREdesign 

%description
Endpoint selection and sample size reassessment for multiple binary
endpoints based on blinded and/or unblinded data. Trial design that allows
an adaptive modification of the primary endpoint based on blinded
information obtained at an interim analysis. The decision rule chooses the
endpoint with the lower estimated required sample size. Additionally, the
sample size is reassessed using the estimated event probabilities and
correlation between endpoints. The implemented design is proposed in
Bofill Roig, M., Gómez Melis, G., Posch, M., and Koenig, F. (2022).
<doi:10.48550/arXiv.2206.09639>.

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
