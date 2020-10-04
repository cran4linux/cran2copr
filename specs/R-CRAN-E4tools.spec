%global packname  E4tools
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Management and Processing Tools for Data Produced by theEmpatica E4

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-DataCombine 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-anytime 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-accelerometry 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-DataCombine 
Requires:         R-CRAN-signal 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-anytime 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-accelerometry 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-doSNOW 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 

%description
Process and manage the data from the Empatica E4. All functions operate on
the EDA data stream, but other streams will be added soon. The Empatica E4
is a wearable physiological monitor made by Empatica (Empatica is not
associated with any of this code). You can find more information about the
E4 at Empatica's website <https://www.empatica.com/research/e4/>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
