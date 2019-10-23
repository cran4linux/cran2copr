%global packname  spatstat.Knet
%global packver   1.11-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.11.2
Release:          1%{?dist}
Summary:          Extension to 'spatstat' for Large Datasets on a Linear Network

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-spatstat >= 1.60.0
BuildRequires:    R-CRAN-spatstat.utils 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-spatstat >= 1.60.0
Requires:         R-CRAN-spatstat.utils 
Requires:         R-Matrix 

%description
Extension to the 'spatstat' package, for analysing large datasets of
spatial points on a network. Provides a memory-efficient algorithm for
computing the geometrically-corrected K function, described in S. Rakshit,
A. Baddeley and G. Nair (2019) <doi:10.18637/jss.v090.i01>

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
