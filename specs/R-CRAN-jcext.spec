%global packname  jcext
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Extended Classification of Weather Types

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-rworldmap 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sp 
Requires:         R-parallel 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-rworldmap 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sp 

%description
Provides a gridded classification of weather types by applying the
Jenkinson and Collison classification. For a given region (it can be
either local region or the whole map),it computes at each grid the 11
weather types during the period considered for the analysis. See Otero et
al., (2017) <doi:10.1007/s00382-017-3705-y> for more information.

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
