%global packname  prettymapr
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Scale Bar, North Arrow, and Pretty Margins in R

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-plyr 

%description
Automates the process of creating a scale bar and north arrow in any
package that uses base graphics to plot in R. Bounding box tools help find
and manipulate extents. Finally, there is a function to automate the
process of setting margins, plotting the map, scale bar, and north arrow,
and resetting graphic parameters upon completion.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/README_files
%{rlibdir}/%{packname}/INDEX
