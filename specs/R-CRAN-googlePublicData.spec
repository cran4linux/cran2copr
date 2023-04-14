%global __brp_check_rpaths %{nil}
%global packname  googlePublicData
%global packver   0.16.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.1
Release:          3%{?dist}%{?buildtag}
Summary:          Working with Google's 'Public Data Explorer' DSPL Metadata Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-readxl 
Requires:         R-CRAN-XML 
Requires:         R-utils 
Requires:         R-CRAN-readxl 

%description
Provides a collection of functions to set up 'Google Public Data Explorer'
<https://www.google.com/publicdata/> data visualization tool with your own
data, building automatically the corresponding DataSet Publishing Language
file, or DSPL (XML), metadata file jointly with the CSV files. All zip-up
and ready to be published in 'Public Data Explorer'.

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
