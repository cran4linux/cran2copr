%global packname  truncdist
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Truncated Random Variables

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.1
Requires:         R-core >= 2.0.1
BuildArch:        noarch
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-evd 
Requires:         R-stats4 
Requires:         R-CRAN-evd 

%description
A collection of tools to evaluate probability density functions,
cumulative distribution functions, quantile functions and random numbers
for truncated random variables.  These functions are provided to also
compute the expected value and variance. Nadarajah and Kotz (2006)
developed most of the functions. QQ plots can be produced. All the
probability functions in the stats, stats4 and evd packages are
automatically available for truncation..

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
