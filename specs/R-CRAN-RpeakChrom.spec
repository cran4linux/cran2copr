%global packname  RpeakChrom
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}
Summary:          Tools for Chromatographic Column Characterization and ModellingChromatographic Peak

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.1
Requires:         R-core >= 2.10.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-ptw 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-ptw 

%description
The quantitative measurement and detection of molecules in HPLC should be
carried out by an accurate description of chromatographic peaks. In this
package non-linear fitting using a modified Gaussian model with a
parabolic variance (PVMG) has been implemented to obtain the retention
time and height at the peak maximum. This package also includes the
traditional Van Deemter approach and two alternatives approaches to
characterize chromatographic column.

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
