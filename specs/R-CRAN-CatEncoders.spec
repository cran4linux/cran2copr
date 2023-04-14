%global __brp_check_rpaths %{nil}
%global packname  CatEncoders
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Encoders for Categorical Variables

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-Matrix >= 1.2.6
BuildRequires:    R-methods 
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-Matrix >= 1.2.6
Requires:         R-methods 

%description
Contains some commonly used categorical variable encoders, such as
'LabelEncoder' and 'OneHotEncoder'. Inspired by the encoders implemented
in Python 'sklearn.preprocessing' package (see
<http://scikit-learn.org/stable/modules/preprocessing.html>).

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
