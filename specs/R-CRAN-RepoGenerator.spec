%global packname  RepoGenerator
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          2%{?dist}
Summary:          Generates a Project and Repo for Easy Initialization of aWorkshop

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-git2r 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-git2r 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-httr 

%description
Generates a project and repo for easy initialization of a GitHub repo for
R workshops. The repo includes a README with instructions to ensure that
all users have the needed packages, an 'RStudio' project with the right
directories and the proper data. The repo can then be used for hosting
code taught during the workshop.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/DownloadData_orig.r
%{rlibdir}/%{packname}/metadata
%doc %{rlibdir}/%{packname}/payload
%{rlibdir}/%{packname}/INDEX
