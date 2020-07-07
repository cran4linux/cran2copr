%global packname  PSPManalysis
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          3%{?dist}
Summary:          Analysis of Physiologically Structured Population Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-pkgbuild >= 1.0
Requires:         R-CRAN-pkgbuild >= 1.0

%description
Performs demographic, bifurcation and evolutionary analysis of
physiologically structured population models, which is a class of models
that consistently translates continuous-time models of individual life
history to the population level. A model of individual life history has to
be implemented specifying the individual-level functions that determine
the life history, such as development and mortality rates and fecundity.
M.A. Kirkilionis, O. Diekmann, B. Lisser, M. Nool, B. Sommeijer & A.M. de
Roos (2001) <doi:10.1142/S0218202501001264>. O.Diekmann, M.Gyllenberg &
J.A.J.Metz (2003) <doi:10.1016/S0040-5809(02)00058-8>. A.M. de Roos (2008)
<doi:10.1111/j.1461-0248.2007.01121.x>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/C
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/Models
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
