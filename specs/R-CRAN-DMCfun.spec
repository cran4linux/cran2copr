%global packname  DMCfun
%global packver   0.12.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.1
Release:          2%{?dist}
Summary:          Diffusion Model of Conflict (DMC) in Reaction Time Tasks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-optimr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-optimr 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
DMC model simulation detailed in Ulrich, R., Schroeter, H., Leuthold, H.,
& Birngruber, T. (2015). Automatic and controlled stimulus processing in
conflict tasks: Superimposed diffusion processes and delta functions.
Cognitive Psychology, 78, 148-174. Ulrich et al. (2015)
<doi:10.1016/j.cogpsych.2015.02.005>.

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
