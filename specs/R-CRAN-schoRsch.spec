%global packname  schoRsch
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}
Summary:          Tools for Analyzing Factorial Experiments

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
Offers a helping hand to psychologists and other behavioral scientists who
routinely deal with experimental data from factorial experiments. It
includes several functions to format output from other R functions
according to the style guidelines of the APA (American Psychological
Association). This formatted output can be copied directly into
manuscripts to facilitate data reporting. These features are backed up by
a toolkit of several small helper functions, e.g., offering out-of-the-box
outlier removal. The package lends its name to Georg "Schorsch"
Schuessler, ingenious technician at the Department of Psychology III,
University of Wuerzburg. For details on the implemented methods, see
Roland Pfister and Markus Janczyk (2016) <doi: 10.20982/tqmp.12.2.p147>.

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
