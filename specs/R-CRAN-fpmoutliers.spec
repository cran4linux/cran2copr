%global packname  fpmoutliers
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Frequent Pattern Mining Outliers

License:          Apache License (== 2.0) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arules >= 1.5.4
BuildRequires:    R-CRAN-pmml 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pryr 
Requires:         R-CRAN-arules >= 1.5.4
Requires:         R-CRAN-pmml 
Requires:         R-CRAN-XML 
Requires:         R-Matrix 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-pryr 

%description
Algorithms for detection of outliers based on frequent pattern mining.
Such algorithms follow the paradigm: if an instance contains more frequent
patterns, it means that this data instance is unlikely to be an anomaly
(He Zengyou, Xu Xiaofei, Huang Zhexue Joshua, Deng Shengchun (2005)
<doi:10.2298/CSIS0501103H>). The package implements a list of existing
state of the art algorithms as well as other published approaches: FPI,
WFPI, FPOF, FPCOF, LFPOF, MFPOF, WCFPOF and WFPOF.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
