%global packname  streambugs
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}
Summary:          Parametric Ordinary Differential Equations Model of Growth,Death, and Respiration of Macroinvertebrate and Algae Taxa

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-deSolve >= 1.20
Requires:         R-CRAN-deSolve >= 1.20

%description
Numerically solve and plot solutions of a parametric ordinary differential
equations model of growth, death, and respiration of macroinvertebrate and
algae taxa dependent on pre-defined environmental factors. The model
(version 1.0) is introduced in Schuwirth, N. and Reichert, P., (2013)
<DOI:10.1890/12-0591.1>. This package includes model extensions and the
core functions introduced and used in Schuwirth, N. et al. (2016)
<DOI:10.1111/1365-2435.12605>, Kattwinkel, M. et al. (2016)
<DOI:10.1021/acs.est.5b04068>, Mondy, C. P., and Schuwirth, N. (2017)
<DOI:10.1002/eap.1530>, and Paillex, A. et al. (2017)
<DOI:10.1111/fwb.12927>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/docs
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
