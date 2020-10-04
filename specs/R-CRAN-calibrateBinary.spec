%global packname  calibrateBinary
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Calibration for Computer Experiments with Binary Responses

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildArch:        noarch
BuildRequires:    R-CRAN-GPfit 
BuildRequires:    R-CRAN-gelnet 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-randtoolbox 
Requires:         R-CRAN-GPfit 
Requires:         R-CRAN-gelnet 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-randtoolbox 

%description
Performs the calibration procedure proposed by Sung et al. (2018+)
<arXiv:1806.01453>. This calibration method is particularly useful when
the outputs of both computer and physical experiments are binary and the
estimation for the calibration parameters is of interest.

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
