%global packname  assist
%global packver   3.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          A Suite of R Functions Implementing Spline Smoothing Techniques

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-nlme 
BuildRequires:    R-lattice 
Requires:         R-nlme 
Requires:         R-lattice 

%description
Fit various smoothing spline models. Includes an ssr() function for
smoothing spline regression, an nnr() function for nonparametric nonlinear
regression, an snr() function for semiparametric nonlinear regression, an
slm() function for semiparametric linear mixed-effects models, and an
snm() function for semiparametric nonlinear mixed-effects models. See Wang
(2011) <doi:10.1201/b10954> for an overview.

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
