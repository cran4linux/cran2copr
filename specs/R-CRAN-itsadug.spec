%global packname  itsadug
%global packver   2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4
Release:          2%{?dist}
Summary:          Interpreting Time Series and Autocorrelated Data Using GAMMs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-mgcv >= 1.8
BuildRequires:    R-CRAN-plotfunctions >= 1.4
Requires:         R-mgcv >= 1.8
Requires:         R-CRAN-plotfunctions >= 1.4

%description
GAMM (Generalized Additive Mixed Modeling; Lin & Zhang, 1999) as
implemented in the R package 'mgcv' (Wood, S.N., 2006; 2011) is a
nonlinear regression analysis which is particularly useful for time course
data such as EEG, pupil dilation, gaze data (eye tracking), and
articulography recordings, but also for behavioral data such as reaction
times and response data. As time course measures are sensitive to
autocorrelation problems, GAMMs implements methods to reduce the
autocorrelation problems. This package includes functions for the
evaluation of GAMM models (e.g., model comparisons, determining regions of
significance, inspection of autocorrelational structure in residuals) and
interpreting of GAMMs (e.g., visualization of complex interactions, and
contrasts).

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

%files
%{rlibdir}/%{packname}
