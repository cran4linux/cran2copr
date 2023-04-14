%global __brp_check_rpaths %{nil}
%global packname  DIFboost
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Detection of Differential Item Functioning (DIF) in Rasch Modelsby Boosting Techniques

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mboost 
BuildRequires:    R-CRAN-penalized 
BuildRequires:    R-CRAN-stabs 
Requires:         R-CRAN-mboost 
Requires:         R-CRAN-penalized 
Requires:         R-CRAN-stabs 

%description
Performs detection of Differential Item Functioning using the method
DIFboost as proposed by Schauberger and Tutz (2016)
<doi:10.1111/bmsp.12060>.

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
%{rlibdir}/%{packname}
