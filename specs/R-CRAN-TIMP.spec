%global packname  TIMP
%global packver   1.13.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.13.2
Release:          3%{?dist}
Summary:          Fitting Separable Nonlinear Models in Spectroscopy andMicroscopy

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-fields >= 4.1
BuildRequires:    R-CRAN-minpack.lm >= 1.1.1
BuildRequires:    R-CRAN-nnls >= 1.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-gclus 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-fields >= 4.1
Requires:         R-CRAN-minpack.lm >= 1.1.1
Requires:         R-CRAN-nnls >= 1.1
Requires:         R-methods 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-colorspace 
Requires:         R-splines 
Requires:         R-CRAN-gclus 
Requires:         R-CRAN-gplots 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
A problem-solving environment (PSE) for fitting separable nonlinear models
to measurements arising in physics and chemistry experiments; has been
extensively applied to time-resolved spectroscopy and FLIM-FRET data.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
