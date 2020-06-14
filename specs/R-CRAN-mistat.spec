%global packname  mistat
%global packver   1.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          2%{?dist}
Summary:          Data Sets, Functions and Examples from the Book: "ModernIndustrial Statistics" by Kenett, Zacks and Amberti

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Provide all the data sets and statistical analysis applications used in
"Modern Industrial Statistics: with applications in R, MINITAB and JMP" by
R.S. Kenett and S. Zacks with contributions by D. Amberti, John Wiley and
Sons, 2013, which is a second revised and expanded revision of "Modern
Industrial Statistics: Design and Control of Quality and Reliability", R.
Kenett and S. Zacks, Duxbury/Wadsworth Publishing, 1998.

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
%doc %{rlibdir}/%{packname}/csvFiles
%doc %{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/INDEX
