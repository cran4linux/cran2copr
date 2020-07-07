%global packname  did
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          3%{?dist}
Summary:          Treatment Effects with Multiple Periods and Groups

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-BMisc >= 1.3.1
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-BMisc >= 1.3.1
Requires:         R-MASS 
Requires:         R-CRAN-pbapply 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-knitr 
Requires:         R-utils 
Requires:         R-CRAN-gridExtra 

%description
The standard Difference-in-Differences (DID) setup involves two periods
and two groups -- a treated group and untreated group.  Many applications
of DID methods involve more than two periods and have individuals that are
treated at different points in time.  This package contains tools for
computing average treatment effect parameters in Difference in Differences
models with more than two periods and with variation in treatment timing
using the methods developed in Callaway and Sant'Anna (2019)
<https://ssrn.com/abstract=3148250>.  The main parameters are group-time
average treatment effects which are the average treatment effect for a
particular group at a a particular time.  These can be aggregated into a
fewer number of treatment effect parameters, and the package deals with
the cases where there is selective treatment timing, dynamic treatment
effects, calendar time effects, or combinations of these.  There are also
functions for testing the Difference in Differences assumption, and
plotting group-time average treatment effects.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
