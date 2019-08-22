%global packname  awspack
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}
Summary:          Amazon Web Services Bundle Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-aws.signature 
BuildRequires:    R-CRAN-aws.ec2metadata 
BuildRequires:    R-CRAN-aws.alexa 
BuildRequires:    R-CRAN-aws.cloudtrail 
BuildRequires:    R-CRAN-aws.iam 
BuildRequires:    R-CRAN-aws.lambda 
BuildRequires:    R-CRAN-aws.polly 
BuildRequires:    R-CRAN-aws.s3 
BuildRequires:    R-CRAN-aws.ses 
BuildRequires:    R-CRAN-aws.sns 
BuildRequires:    R-CRAN-aws.sqs 
Requires:         R-CRAN-aws.signature 
Requires:         R-CRAN-aws.ec2metadata 
Requires:         R-CRAN-aws.alexa 
Requires:         R-CRAN-aws.cloudtrail 
Requires:         R-CRAN-aws.iam 
Requires:         R-CRAN-aws.lambda 
Requires:         R-CRAN-aws.polly 
Requires:         R-CRAN-aws.s3 
Requires:         R-CRAN-aws.ses 
Requires:         R-CRAN-aws.sns 
Requires:         R-CRAN-aws.sqs 

%description
A bundle of all of 'cloudyr' project <http://cloudyr.github.io/> packages
for Amazon Web Services ('AWS') <https://aws.amazon.com/>. It depends upon
all of the 'cloudyr' project's 'AWS' packages. It is mainly useful for
installing the entire suite of packages; more likely than not you will
only want to load individual packages one at a time.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
