%global __brp_check_rpaths %{nil}
%global packname  VFS
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Vegetated Filter Strip and Erosion Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nleqslv >= 3.3.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-e1071 
Requires:         R-CRAN-nleqslv >= 3.3.0
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-e1071 

%description
Empirical models for runoff, erosion, and phosphorus loss across a
vegetated filter strip, given slope, soils, climate, and vegetation (Gall
et al., 2018) <doi:10.1007/s00477-017-1505-x>. It also includes functions
for deriving climate parameters from measured daily weather data, and for
simulating rainfall. Models implemented include MUSLE (Williams, 1975) and
APLE (Vadas et al., 2009 <doi:10.2134/jeq2008.0337>).

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
