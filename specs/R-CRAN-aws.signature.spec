%global __brp_check_rpaths %{nil}
%global packname  aws.signature
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          3%{?dist}%{?buildtag}
Summary:          Amazon Web Services Request Signatures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-base64enc 

%description
Generates version 2 and version 4 request signatures for Amazon Web
Services ('AWS') <https://aws.amazon.com/> Application Programming
Interfaces ('APIs') and provides a mechanism for retrieving credentials
from environment variables, 'AWS' credentials files, and 'EC2' instance
metadata. For use on 'EC2' instances, users will need to install the
suggested package 'aws.ec2metadata'
<https://cran.r-project.org/package=aws.ec2metadata>.

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
