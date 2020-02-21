%global packname  dssd
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Distance Sampling Survey Design

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-methods 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-rgdal 
Requires:         R-methods 

%description
Creates survey designs for distance sampling surveys. These designs can be
assessed for various effort and coverage statistics. Once the user is
satisfied with the design characteristics they can generate a set of
transects to use in their distance sampling survey. Many of the designs
implemented in this R package were first made available in our 'Distance'
for Windows software and are detailed in Chapter 7 of Advanced Distance
Sampling, Buckland et. al. (2008, ISBN-13: 978-0199225873). Find out more
about estimating animal/plant abundance with distance sampling at
<http://distancesampling.org/>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
