%global __brp_check_rpaths %{nil}
%global packname  elitism
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Equipment for Logarithmic and Linear Time Stepwise MultipleHypothesis Testing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
Requires:         R-stats 
Requires:         R-MASS 

%description
Recently many new p-value based multiple test procedures have been
proposed, and these new methods are more powerful than the widely used
Hochberg procedure. These procedures strongly control the familywise error
rate (FWER). This is a comprehensive collection of p-value based
FWER-control stepwise multiple test procedures, including six procedure
families and thirty multiple test procedures. In this collection, the
conservative Hochberg procedure, linear time Hommel procedures, asymptotic
Rom procedure, Gou-Tamhane-Xi-Rom procedures, and Quick procedures are all
developed in recent five years since 2014. The package name "elitism" is
an acronym of "e"quipment for "l"ogarithmic and l"i"near "ti"me "s"tepwise
"m"ultiple hypothesis testing. Version 1.0.0 was released on June 26,
2019. See Gou, J., and Zhang, F. (2020). Quick multiple test procedures
and p-value adjustments. Technical report.

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
%{rlibdir}/%{packname}/INDEX
