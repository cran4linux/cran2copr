%global packname  longCatEDA
%global packver   0.31
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.31
Release:          3%{?dist}
Summary:          Package for Plotting Categorical Longitudinal and Time-SeriesData

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-stats 

%description
Methods for plotting categorical longitudinal and time-series data by
mapping individuals to the vertical space (each horizontal line represents
a participant), time (or repeated measures) to the horizontal space,
categorical (or discrete) states as facets using color or shade, and
events to points using plotting characters. Sorting individuals in the
vertical space and (or) stratifying them by groups can reveal patterns in
the changes over time.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
