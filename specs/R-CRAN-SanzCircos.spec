%global packname  SanzCircos
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Functions for Creating 'Circos' Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-randomcoloR 
BuildRequires:    R-parallel 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-randomcoloR 
Requires:         R-parallel 
Requires:         R-grDevices 

%description
A series of functions designed to aid in the creation of input files for
the 'Circos' visualization platform <http://circos.ca/>. Included are two
main function types - make_circos_x() and write_circos_x(). The "make"
functions are designed to process an input data set, and return a data
frame that can be manipulated and filtered to eliminate the need to write
Perl scripts within the 'Circos' software platform for data filtering. The
"write" functions take processed data frames from the "make" functions,
and write .txt files compatible with the 'Circos' platform. In addition to
these function types, there are other accessory functions that aid in the
manipulation of the make_circos_x() returned data frames to enhance final
visual appeal (such as color_circos_links()).

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
%{rlibdir}/%{packname}/INDEX
