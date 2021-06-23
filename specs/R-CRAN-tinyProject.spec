%global __brp_check_rpaths %{nil}
%global packname  tinyProject
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          3%{?dist}%{?buildtag}
Summary:          A Lightweight Template for Data Analysis Projects

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-brew 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R.utils 
Requires:         R-CRAN-brew 
Requires:         R-methods 
Requires:         R-CRAN-R.utils 

%description
Creates useful files and folders for data analysis projects and provides
functions to manage data, scripts and output files. Also provides a
project template for 'Rstudio'.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/Rprofile.brew
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/scriptTemplates
%{rlibdir}/%{packname}/INDEX
