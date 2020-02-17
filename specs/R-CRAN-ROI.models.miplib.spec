%global packname  ROI.models.miplib
%global packver   0.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}
Summary:          R Optimization Infrastructure: 'MIPLIB' 2010 Benchmark Instances

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ROI >= 0.2.0
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-Rglpk 
Requires:         R-CRAN-ROI >= 0.2.0
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-Rglpk 

%description
The mixed integer programming library 'MIPLIB' (see
<http://miplib.zib.de/>) is commonly used to compare the performance of
mixed integer optimization solvers. This package provides functions to
access 'MIPLIB' from the 'R' Optimization Infrastructure ('ROI'). More
information about 'MIPLIB' can be found in the paper by Koch et al.
available at <http://mpc.zib.de/index.php/MPC/article/viewFile/56/28>. The
'README.md' file illustrates how to use this package.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/roi_op
%{rlibdir}/%{packname}/INDEX
