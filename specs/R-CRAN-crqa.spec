%global packname  crqa
%global packver   1.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          1%{?dist}
Summary:          Cross-Recurrence Quantification Analysis for Categorical andContinuous Time-Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-tseriesChaos 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-pracma 
Requires:         R-Matrix 
Requires:         R-CRAN-tseriesChaos 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-pracma 

%description
Cross-recurrence quantification analysis of two time-series, of either
categorical or continuous values. It provides different methods for
profiling cross-recurrence, i.e., only looking at the diagonal recurrent
points, as well as more in-depth measures of the whole cross-recurrence
plot, e.g., recurrence rate. Please refer to by Coco and Dale (2014)
<doi:10.3389/fpsyg.2014.00510> for further details about the method.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
