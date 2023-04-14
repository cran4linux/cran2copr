%global __brp_check_rpaths %{nil}
%global packname  unisensR
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          3%{?dist}%{?buildtag}
Summary:          Read 'Unisens' Data

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 1.0.0
BuildRequires:    R-CRAN-hexView 
BuildRequires:    R-CRAN-vroom 
Requires:         R-CRAN-XML >= 1.0.0
Requires:         R-CRAN-hexView 
Requires:         R-CRAN-vroom 

%description
Provides the ability to read 'Unisens' data into R. 'Unisens' is a
universal data format for multi sensor data.

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
