%global __brp_check_rpaths %{nil}
%global packname  aprof
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          3%{?dist}%{?buildtag}
Summary:          Amdahl's Profiler, Directed Optimization Made Easy

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-testthat 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-testthat 

%description
Assists the evaluation of whether and where to focus code optimization,
using Amdahl's law and visual aids based on line profiling. Amdahl's
profiler organizes profiling output files (including memory profiling) in
a visually appealing way. It is meant to help to balance development vs.
execution time by helping to identify the most promising sections of code
to optimize and projecting potential gains. The package is an addition to
R's standard profiling tools and is not a wrapper for them.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
