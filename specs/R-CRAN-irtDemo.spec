%global __brp_check_rpaths %{nil}
%global packname  irtDemo
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Item Response Theory Demo Collection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildArch:        noarch
BuildRequires:    R-CRAN-fGarch >= 3010.82
BuildRequires:    R-CRAN-shiny >= 0.13.2
Requires:         R-CRAN-fGarch >= 3010.82
Requires:         R-CRAN-shiny >= 0.13.2

%description
Includes a collection of shiny applications to demonstrate or to explore
fundamental item response theory (IRT) concepts such as estimation,
scoring, and multidimensional IRT models.

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
