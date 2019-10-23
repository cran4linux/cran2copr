%global packname  factorial2x2
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Design and Analysis of 2x2 Factorial Trial

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-survival 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 

%description
Used for the design and analysis of a 2x2 factorial trial for a
time-to-event endpoint.  Performs power calculations and significance
testing.  Important reference papers include Slud EV. (1994)
<https://www.ncbi.nlm.nih.gov/pubmed/8086609> Lin DY, Gong J, Gallo P,
Bunn PH, Couper D. (2016) <DOI:10.1111/biom.12507> Leifer ES, Troendle JF,
Kolecki A, Follmann DA. (2019)
<https://github.com/EricSLeifer/factorial2x2/blob/master/Leifer%20et%20al%20Factorial.pdf>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
