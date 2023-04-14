%global __brp_check_rpaths %{nil}
%global packname  aws.iam
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          3%{?dist}%{?buildtag}
Summary:          AWS IAM Client Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-aws.signature >= 0.3.4
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-aws.signature >= 0.3.4
Requires:         R-utils 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-jsonlite 

%description
A simple client for the Amazon Web Services ('AWS') Identity and Access
Management ('IAM') 'API' <https://aws.amazon.com/iam/>.

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
