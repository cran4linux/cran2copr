%global packname  lcmm
%global packver   1.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.2
Release:          2%{?dist}
Summary:          Extended Mixed Models Using Latent Classes and Latent Processes

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-survival >= 2.37.2
BuildRequires:    R-parallel 
Requires:         R-survival >= 2.37.2
Requires:         R-parallel 

%description
Estimation of various extensions of the mixed models including latent
class mixed models, joint latent latent class mixed models and mixed
models for curvilinear univariate or multivariate longitudinal outcomes
using a maximum likelihood estimation method (Proust-Lima, Philipps,
Liquet (2017) <doi:10.18637/jss.v078.i02>).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
