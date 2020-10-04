%global packname  ari
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          3%{?dist}%{?buildtag}
Summary:          Automated R Instructor

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-text2speech >= 0.2.8
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-CRAN-webshot 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-hms 
Requires:         R-CRAN-text2speech >= 0.2.8
Requires:         R-CRAN-tuneR 
Requires:         R-CRAN-webshot 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-rvest 
Requires:         R-tools 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-hms 

%description
Create videos from 'R Markdown' documents, or images and audio files.
These images can come from image files or HTML slides, and the audio files
can be provided by the user or computer voice narration can be created
using 'Amazon Polly'. The purpose of this package is to allow users to
create accessible, translatable, and reproducible lecture videos. See
<https://aws.amazon.com/polly/> for more information.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/test
%{rlibdir}/%{packname}/INDEX
