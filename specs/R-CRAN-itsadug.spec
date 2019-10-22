%global packname  itsadug
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          1%{?dist}
Summary:          Interpreting Time Series and Autocorrelated Data Using GAMMs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-mgcv >= 1.8
BuildRequires:    R-CRAN-plotfunctions >= 1.3
Requires:         R-mgcv >= 1.8
Requires:         R-CRAN-plotfunctions >= 1.3

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


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
