%global packname  SBRect
%global packver   0.26
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.26
Release:          2%{?dist}
Summary:          Detecting structural breaks using rectangle covering(non-parametric method).

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava 
Requires:         R-CRAN-rJava 

%description
The package uses fitting axes-aligned rectangles to a time series in order
to find structural breaks. The algorithm enclose the time series in a
number of axes-aligned rectangles and tries to minimize their area and
number. As these are conflicting aims, the user has to specify a parameter
alpha in [0.0,1.0]. Values close to 0 result in more breakpoints, values
close to 1 in fewer. The left edges of the rectangles are the breakpoints.
The package supplies two methods, computeBreakPoints(series,alpha) which
returns the indices of the break points and
computeRectangles(series,alpha) which returns the rectangles. The
algorithm is randomised; it uses a genetic algorithm. Therefore, the break
point sequence found can be different in different executions of the
method on the same data, especially when used on longer series of some
thousand observations. The algorithm uses a range-tree as background data
structure which makes i very fast and suited to analyse series with
millions of observations. A detailed description can be found in Paul
Fischer, Astrid Hilbert, Fast detection of structural breaks, Proceedings
of Compstat 2014.

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
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
