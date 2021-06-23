%global __brp_check_rpaths %{nil}
%global packname  FuncMap
%global packver   1.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.10
Release:          3%{?dist}%{?buildtag}
Summary:          Hive Plots of R Package Function Calls

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvbutils 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-CRAN-mvbutils 

%description
Analyzes the function calls in an R package and creates a hive plot of the
calls, dividing them among functions that only make outgoing calls
(sources), functions that have only incoming calls (sinks), and those that
have both incoming calls and make outgoing calls (managers).  Function
calls can be mapped by their absolute numbers, their normalized absolute
numbers, or their rank.  FuncMap should be useful for comparing packages
at a high level for their overall design.  Plus, it's just plain fun.  The
hive plot concept was developed by Martin Krzywinski (www.hiveplot.com)
and inspired this package.  Note: this package is maintained for
historical reasons. HiveR is a full package for creating hive plots.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
