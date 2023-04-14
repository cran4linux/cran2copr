%global __brp_check_rpaths %{nil}
%global packname  covfefe
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Covfefy Any Word, Sentence or Speech

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tokenizers 
Requires:         R-CRAN-tokenizers 

%description
Converts any word, sentence or speech into Trump's infamous "covfefe"
format. Reference:
<https://www.nytimes.com/2017/05/31/us/politics/covfefe-trump-twitter.html>.
Inspiration thanks to:
<https://codegolf.stackexchange.com/questions/123685/covfefify-a-string>.

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
