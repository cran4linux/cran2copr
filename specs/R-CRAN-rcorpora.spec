%global __brp_check_rpaths %{nil}
%global packname  rcorpora
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          A Collection of Small Text Corpora of Interesting Data

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-jsonlite 

%description
A collection of small text corpora of interesting data. It contains all
data sets from 'dariusk/corpora'. Some examples: names of animals: birds,
dinosaurs, dogs; foods: beer categories, pizza toppings; geography:
English towns, rivers, oceans; humans: authors, US presidents,
occupations; science: elements, planets; words: adjectives, verbs,
proverbs, US president quotes.

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
