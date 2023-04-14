%global __brp_check_rpaths %{nil}
%global packname  MNM
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Multivariate Nonparametric Methods. An Approach Based on SpatialSigns and Ranks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.2
Requires:         R-core >= 2.9.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ICSNP 
BuildRequires:    R-CRAN-SpatialNP 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-ICS 
Requires:         R-CRAN-ICSNP 
Requires:         R-CRAN-SpatialNP 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-ICS 

%description
Multivariate tests, estimates and methods based on the identity score,
spatial sign score and spatial rank score are provided. The methods
include one and c-sample problems, shape estimation and testing, linear
regression and principal components. The methodology is described in Oja
(2010) <doi:10.1007/978-1-4419-0468-3> and Nordhausen and Oja (2011)
<doi:10.18637/jss.v043.i05>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
